import argparse


def parse_opts():

    parser = argparse.ArgumentParser()

    # Dataset
    parser.add_argument('--dataset', type=str, required=True, help='Dataset string (kinetics | activitynet | ucf101 | blender)')
    parser.add_argument('--video_path', type=str, required=True, help='Path to location of dataset videos')
    parser.add_argument('--annotation_path', type=str, required=False, help='Path to location of dataset annotation file')
    parser.add_argument('--num_val_samples', type=int, default=3, help='Number of validation samples for each activity')

    parser.add_argument('--norm_value', default=255, type=int, help='Divide inputs by 255 or 1')

    parser.add_argument('--num_classes', default=400, type=int, help= 'Number of classes (activitynet: 200, kinetics: 400, ucf101: 101, hmdb51: 51)')
    parser.add_argument('--spatial_size', default=224, type=int, help='Height and width of inputs')
    parser.add_argument('--temporal_size', default=64, type=int, help='Temporal duration of inputs')

    # Finetuning
    parser.add_argument('--resume_path', default='', type=str, help='Checkpoint file (.pth) of previous training')
    parser.add_argument('--num_finetune_classes', default=36, type=int, help='Number of classes for fine-tuning. n_classes is set to the number when pretraining.')
    parser.add_argument('--finetune_prefixes', default='logits,Mixed_5', type=str, help='Prefixes of layers to finetune, comma seperated.')

    # Optimization
    parser.add_argument('--optimizer', default='adam', type=str, help='Which optimizer to use (SGD | adam | rmsprop)')
    parser.add_argument('--learning_rate', default=0.01, type=float, help='Initial learning rate (divided by 10 while training by lr-scheduler)')
    parser.add_argument('--momentum', default=0.9, type=float, help='Momentum')
    parser.add_argument('--weight_decay', default=1e-7, type=float, help='Weight Decay')
    parser.add_argument('--batch_size', default=32, type=int, help='Batch Size')
    parser.add_argument('--dropout_keep_prob', default=1.0, type=float, help='Dropout keep probability')
    parser.add_argument('--num_epochs', default=20, type=int, help='Number of epochs to train for')

    # Misc
    parser.add_argument('--device', default='cuda:0', help='Device string cpu | cuda:0')
    parser.add_argument('--history_steps', default=25, type=int, help='History of running average meters')
    parser.add_argument('--num_workers', default=4, type=int, help='Number of threads for multi-thread loading')
    parser.add_argument('--no_eval', action='store_true', default=False, help='Disable evaluation')
    parser.add_argument('--save_path', default='./checkpoints/', type=str, help='Where to save checkpoint files.')

    return parser.parse_args()