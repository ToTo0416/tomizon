<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>クリックゲーム</title>
  <style>
    #button {
      font-size: 24px;
      padding: 20px;
    }
  </style>
</head>
<body>
  <h1>クリックゲーム</h1>
  <button id="button">クリック！</button>
  <p>スコア: <span id="score">0</span></p>

  <script>
    let score = 0;
    const button = document.getElementById("button");
    const scoreDisplay = document.getElementById("score");

    button.addEventListener("click", () => {
      score++;
      scoreDisplay.textContent = score;
    });
  </script>
</body>
</html>
