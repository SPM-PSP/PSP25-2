from operator import itemgetter
from mmaction.apis import init_recognizer, inference_recognizer
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# config、checkpoint、label 文件都在 Backend/app/utils/Model 下
config_file = os.path.join(BASE_DIR, 'config.py')
checkpoint_file = os.path.join(BASE_DIR, 'tsn_imagenet-pretrained-r50_8xb32-1x1x8-100e_kinetics400-rgb_20220906-2692d16c.pth')
label_file = os.path.join(BASE_DIR, 'label_map_k400.txt')

# 图片目录在 Backend/data/video 下
img_dir = os.path.abspath(os.path.join(BASE_DIR, '..', '..', '..', 'data', 'video'))

input_dict = dict(
    frame_dir=img_dir,
    filename_tmpl='frame_{:02d}.jpg',
    start_index=1,
    modality='RGB',
    total_frames=30
)

model = init_recognizer(config_file, checkpoint_file, device='cuda:0')

pred_result = inference_recognizer(model, input_dict)

pred_scores = pred_result.pred_score.tolist()
score_tuples = tuple(zip(range(len(pred_scores)), pred_scores))
score_sorted = sorted(score_tuples, key=itemgetter(1), reverse=True)
top5_label = score_sorted[:5]

with open(label_file, encoding='utf-8') as f:
    labels = [x.strip() for x in f.readlines()]
results = [(labels[k[0]], k[1]) for k in top5_label]

print('The top-5 labels with corresponding scores are:')
for result in results:
    print(f'{result[0]}: ', result[1])