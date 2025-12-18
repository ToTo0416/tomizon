<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <title>服装生成アプリ</title>
  <style>
    body { font-family: sans-serif; background:#f0f0f0; text-align:center; }
    #controls { margin:20px; }
    #out { border:1px solid #ccc; background:#fff; display:inline-block; }
  </style>
</head>
<body>
  <h1>服装生成アプリ (簡略版)</h1>
  <div id="controls">
    色相: <input id="hue" type="range" min="0" max="359" value="210">
    トーン:
    <select id="tone">
      <option value="soft">soft</option>
      <option value="bold">bold</option>
    </select>
    柄:
    <select id="pattern">
      <option value="none">なし</option>
      <option value="stripe">ストライプ</option>
      <option value="check">チェック</option>
    </select>
    <button onclick="render()">生成</button>
  </div>
  <div id="out"></div>

  <script>
    function hsl(h,s,l){ return `hsl(${h},${s}%,${l}%)`; }
    function complement(h){ return (h+180)%360; }

    function stripePattern(id,c1,c2){
      return `<pattern id="${id}" patternUnits="userSpaceOnUse" width="12" height="12">
        <rect width="12" height="12" fill="${c1}"/>
        <rect x="0" y="0" width="6" height="12" fill="${c2}"/>
      </pattern>`;
    }
    function checkPattern(id,c1,c2){
      return `<pattern id="${id}" patternUnits="userSpaceOnUse" width="16" height="16">
        <rect width="16" height="16" fill="${c1}"/>
        <rect x="0" y="0" width="8" height="8" fill="${c2}"/>
        <rect x="8" y="8" width="8" height="8" fill="${c2}"/>
      </pattern>`;
    }

    function generateOutfit(hue,tone,pattern){
      const base = hsl(hue,50,tone==='soft'?70:50);
      const accent = hsl(complement(hue),60,tone==='soft'?40:35);
      const neutral = hsl(hue,15,90);
      const pid = pattern!=="none" ? "p1" : null;
      const defs = pid ? (pattern==="stripe"?stripePattern(pid,base,accent):checkPattern(pid,base,accent)) : "";
      const topFill = pid?`url(#${pid})`:base;

      return `<svg width="400" height="360" xmlns="http://www.w3.org/2000/svg">
        <defs>${defs}</defs>
        <rect x="0" y="0" width="400" height="360" fill="#fafafa"/>
        <rect x="40" y="40" width="320" height="220" rx="30" fill="${neutral}" stroke="#333" stroke-width="2"/>
        <path d="M 90 60 c 24 0, 48 20, 60 40 v 60 c 0 20,-60 30,-60 30 h -40 c -60 0,-60 -30,-60 -30 v -60 c 12 -20, 36 -40, 60 -40 Z"
          fill="${topFill}" stroke="#333" stroke-width="2"/>
        <path d="M 120 210 h 160 v 70 c -20 20,-80 20,-80 20 c -60 0,-80 0,-80 -20 v -70 Z"
          fill="${accent}" stroke="#333" stroke-width="2"/>
      </svg>`;
    }

    function render(){
      const hue = parseInt(document.getElementById("hue").value,10);
      const tone = document.getElementById("tone").value;
      const pattern = document.getElementById("pattern").value;
      document.getElementById("out").innerHTML = generateOutfit(hue,tone,pattern);
    }
    render();
  </script>
</body>
</html>
