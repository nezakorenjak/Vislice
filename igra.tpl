% import model

<!DOCTYPE html>
<html>

<head>
<title>Vislice</title>
</head>


<body>


<h1>{{ igra.pravilni_del_gesla() }}</h1>


<h2>Poskusili ste že: </h2>

% if poskus == model.ZMAGA or poskus == model.PORAZ:


<form action="/igra/" method="post">
  <button type="submit">Nova igra</button>
</form>

% else:
<form action="/igra/{{id_igre}}/" method="post">
  <input type="text" name="poskus">
  <input type="submit" value="Ugibaj">
</form>
%end



</body>

</html>