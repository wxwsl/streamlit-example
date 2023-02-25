<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>获取地理位置</title>
</head>
<body>
  <p>点击下面的按钮获取您的位置：</p>
  <button onclick="getLocation()">获取位置</button>
  <p id="location"></p>
  
  <script>
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
      } else {
        document.getElementById("location").innerHTML = "您的浏览器不支持获取位置信息。";
      }
    }

    function showPosition(position) {
      var latitude = position.coords.latitude;
      var longitude = position.coords.longitude;
      document.getElementById("location").innerHTML = "您的位置是：" + latitude + ", " + longitude;
    }
  </script>
</body>
</html>
