"""Function to train a model."""
from time import time
from typing import Optional

import numpy as np
from tensorflow.keras.callbacks import EarlyStopping
# Hide lines below until Lab 3
import wandb
from wandb.keras import WandbCallback
# Hide lines above until Lab 3

from text_recognizer.datasets.dataset import Dataset
from text_recognizer.models.base import Model


EARLY_STOPPING = True


def train_model(
        model: Model,
        dataset: Dataset,
        epochs: int,
        batch_size: int,
        gpu_ind: Optional[int] = None,
        use_wandb: bool = False) -> Model:
    """Train model."""
    callbacks = []

    if EARLY_STOPPING:
        early_stopping = EarlyStopping(monitor='val_loss', min_delta=0.01, patience=3, verbose=1, mode='auto')
        callbacks.append(early_stopping)

    # Hide lines below until Lab 3
    if use_wandb:
        wandb.init()
        wandb_callback = WandbCallback()
        callbacks.append(wandb_callback)
    # Hide lines above until Lab 3

    model.network.summary()

    t = time()
    _history = model.fit(dataset=dataset, batch_size=batch_size, epochs=epochs, callbacks=callbacks)
    print('Training took {:2f} s'.format(time() - t))

    return model
