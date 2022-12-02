<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<h1>OpenCV Mobile App</h1>

<form id="take_picture" action='process.php' method='post' enctype="multipart/form-data">
<input type="file" accept="image/*" capture="camera" name="picture" value="Take Picture" />
</form>


<script type="text/javascript">
  document.getElementById("take_picture").onchange = function() {
      // submitting the form
      document.getElementById("take_picture").submit();
  };
</script>
