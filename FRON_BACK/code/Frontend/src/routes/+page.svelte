<script>
  let imgSrc = 'http://127.0.0.1:5000/video/display?ts=' + Date.now();

  function refresh() {
    imgSrc = 'http://127.0.0.1:5000/video/display?ts=' + Date.now();
  }

  // 每0.1秒刷新一次图片
  let timer;
  import { onMount, onDestroy } from 'svelte';
  onMount(() => {
    timer = setInterval(refresh, 100);
  });
  onDestroy(() => {
    clearInterval(timer);
  });
</script>

<div style="display: flex; flex-direction: column; align-items: center; margin-top: 2rem;">
  <h2>摄像头实时画面</h2>
  <img src={imgSrc} alt="实时画面" style="width: 640px; height: 480px; border: 1px solid #ccc;" />
</div>