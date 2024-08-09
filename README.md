# Self-Supervised Learning for Monocular Depth Estimation from Aerial Imagery
> Supervised learning based methods for monocular depth estimation usually require large amounts of extensively annotated training data. 
In the case of aerial imagery, this ground truth is particularly difficult to acquire. 
Therefore, in this paper we present a method for self-supervised learning for monocular depth estimation from aerial imagery that does not require annotated training data. 
For this, we only use an image sequence from a single moving camera and learn to simultaneously estimate depth and pose information. 
By sharing the weights between pose and depth estimation, we achieve a relatively small model, which favors real-time application. 
<img src='results_on_synthetic_dataset.png' width=1000>


Install packages :
```bash
pip install -r requirements.txt
```

To prepare data we used code from https://github.com/tinghuiz/SfMLearner/

```bash
python data/prepare_train_data.py --dataset_dir=<path-to-dataset-dir> --dump_root=<path-to-dump-dir> --seq_length=3 --img_width=384 --img_height=224 --num_threads=16 --frame_offset <offset-between-frames>
```

## Training

```bash
python train.py --dataset_dir=<path-to-dump-dir> --checkpoint_dir=<-where-to-store-checkpoints> --img_width=384 --img_height=224 --batch_size=20
```
You can then start a tensorboard session by
```bash
tensorboard --logdir=<-where-to-store-checkpoints>
```
