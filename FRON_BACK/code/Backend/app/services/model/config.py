
model = dict(
    type='Recognizer2D',
    backbone=dict(
        type='ResNet',
        depth=50,
        norm_eval=False,
        pretrained='https://download.pytorch.org/models/resnet50-11ad3fa6.pth'
    ),
    cls_head=dict(
        type='TSNHead',
        num_classes=400,
        in_channels=2048,
        spatial_type='avg',
        consensus=dict(type='AvgConsensus', dim=1),
        dropout_ratio=0.4,
        init_std=0.01,
        average_clips='prob'
    ),
    data_preprocessor=dict(
        type='ActionDataPreprocessor',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        format_shape='NCHW'
    ),
    test_cfg=None
)

default_scope = 'mmaction'

test_pipeline = [
    dict(type='SampleFrames', clip_len=1, frame_interval=1, num_clips=30, test_mode=True),
    dict(type='RawFrameDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='TenCrop', crop_size=224),
    dict(type='FormatShape', input_format='NCHW'),
    dict(type='PackActionInputs')
]