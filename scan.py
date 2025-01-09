from typing import Any, Dict, List, Tuple, Union
import os
import shutil
from modelscan.modelscan import ModelScan

try:
    import tensorflow as tf
except ImportError:
    pass
try:
    import torch as T
except ImportError:
    pass
import pandas as pd


class Scan:
    def __init__(self):
        super().__init__()
        self.model_scan = ModelScan()

    @staticmethod
    def _delete_temp_model(model_path: str) -> None:
        current_path = os.getcwd()
        if os.path.exists(current_path + '/' + model_path + '_temp'):
            shutil.rmtree(current_path + '/' + model_path + '_temp')

    def scan(self, model_path: str, verbose: bool = False) -> Tuple[bool, pd.DataFrame]:
        results = self.model_scan.scan(model_path)
        df = pd.DataFrame(results['issues'], columns=['severity', 'operator', 'description'])
        if verbose:
            print(df)
        safe = True if df.empty else False
        return safe, df

    def scan_load(self, model_path: str, framework: str = 'tensorflow', verbose: bool = False):
        safe, df = self.scan(model_path, verbose=verbose)
        if not safe:
            if verbose:
                print('Model not safe to load')
                print(df)
            return None, df
        if framework == 'tensorflow' or framework == 'keras' or framework == 'tf':
            model = tf.keras.models.load_model(model_path)
        elif framework == 'pytorch':
            model = T.load(model_path)
        else:
            raise ValueError('Framework not supported')
        if verbose:
            print('Model loaded successfully')
        return model, df

    def scan_save(self, model: Any, model_path: str, framework='tensorflow', verbose: bool = False) -> bool:
        if framework == 'tensorflow':
            model.save(model_path + '_temp')
        elif framework == 'pytorch':
            T.save(model, model_path + '_temp')
        else:
            raise ValueError('Framework not supported')
        if verbose:
            print('Current Model saved temporarily for scanning')
        safe, df = self.scan(model_path + '_temp', verbose=verbose)
        if not safe:
            print('Model not safe to save')
            print(df)
            # Delete temporary model from disk
            self._delete_temp_model(model_path)
            return False
        # Delete temporary model from disk
        self._delete_temp_model(model_path)
        if verbose:
            print('Temporary Model deleted successfully')
        if framework == 'tensorflow':
            model.save(model_path)
        elif framework == 'pytorch':
            T.save(model, model_path)
        if verbose:
            print('Model saved successfully')
        return True


if __name__ == '__main__':
    scan = Scan()
    model_path = 'models/iomodel'
    model, frame = scan.scan_load(model_path, verbose=False)
    print(frame)
    if model is not None:
        scan.scan_save(model, model_path, verbose=True)

