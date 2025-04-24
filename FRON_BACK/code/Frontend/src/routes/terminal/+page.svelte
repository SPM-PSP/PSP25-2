<script>
    let imgSrc = 'http://127.0.0.1:5000/video/display?ts=' + Date.now();
  
    function refresh() {
      imgSrc = 'http://127.0.0.1:5000/video/display?ts=' + Date.now();
    }
  
    let timer;
    import { onMount, onDestroy } from 'svelte';
    onMount(() => {
      timer = setInterval(refresh, 100);
    });
    onDestroy(() => {
      clearInterval(timer);
    });
  </script>
  
  <style>
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 3rem;
      background: #f8fafc;
      border-radius: 18px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
      padding: 2.5rem 2rem 2rem 2rem;
      max-width: 740px;
      margin-left: auto;
      margin-right: auto;
    }
    .title {
      font-size: 2rem;
      font-weight: 700;
      color: #2563eb;
      margin-bottom: 1.5rem;
      letter-spacing: 1px;
    }
    .img-wrapper {
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.06);
      padding: 1rem;
      border: 1.5px solid #e5e7eb;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .camera-img {
      width: 640px;
      height: 480px;
      object-fit: cover;
      border-radius: 8px;
      border: 1.5px solid #d1d5db;
      background: #e5e7eb;
      transition: box-shadow 0.2s;
      box-shadow: 0 1px 8px rgba(37,99,235,0.08);
    }
    @media (max-width: 700px) {
      .camera-img {
        width: 98vw;
        height: auto;
        max-width: 98vw;
        max-height: 60vw;
      }
      .container {
        padding: 1rem;
      }
    }
  </style>
  
  <div class="container">
    <div class="title">摄像头实时画面</div>
    <div class="img-wrapper">
      <img class="camera-img" src={imgSrc} alt="实时画面" />
    </div>
  </div>