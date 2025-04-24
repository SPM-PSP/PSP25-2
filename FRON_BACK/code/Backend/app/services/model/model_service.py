import os
import time
import json
from operator import itemgetter
from mmaction.apis import init_recognizer, inference_recognizer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config_file = os.path.join(BASE_DIR, 'config.py')
checkpoint_file = os.path.join(BASE_DIR, 'tsn_imagenet-pretrained-r50_8xb32-1x1x8-100e_kinetics400-rgb_20220906-2692d16c.pth')
label_file = os.path.join(BASE_DIR, 'label_map_k400.txt')

img_dir = os.path.abspath(os.path.join(BASE_DIR, '..', '..', '..', 'data', 'video'))
result_dir = os.path.abspath(os.path.join(BASE_DIR, '..', '..', '..', 'data', 'result'))
os.makedirs(result_dir, exist_ok=True)
result_path = os.path.join(result_dir, 'result.json')

input_dict = dict(
    frame_dir=img_dir,
    filename_tmpl='frame_{:02d}.jpg',
    start_index=1,
    modality='RGB',
    total_frames=30
)

with open(label_file, encoding='utf-8') as f:
    labels = [x.strip() for x in f.readlines()]

model = init_recognizer(config_file, checkpoint_file, device='cuda:0')

def run_inference_service(interval=3):
    """持续推理服务，将top5结果写入result.json"""
    while True:
        try:
            pred_result = inference_recognizer(model, input_dict)
            pred_scores = pred_result.pred_score.tolist()
            score_tuples = tuple(zip(range(len(pred_scores)), pred_scores))
            score_sorted = sorted(score_tuples, key=itemgetter(1), reverse=True)
            top5_label = score_sorted[:5]
            results = [{"label": labels[k[0]], "score": float(k[1])} for k in top5_label]
            with open(result_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
                f.close()
        except Exception as e:
            print(f"Inference error: {e}")
        time.sleep(interval)