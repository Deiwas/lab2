<html>
   <head>
      <title>
         Тестируем PHP
      </title>
   </head>
   <body>
   <?php 
      /* Подключение к серверу MySQL */ 
	$link = mysqli_connect( 
        'localhost',  /* Хост, к которому мы подключаемся */ 
        'root',       /* Имя пользователя */ 
        '',   /* Используемый пароль */ 
        'op5');     /* База данных для запросов по умолчанию */ 

	if (!$link) { 
   		printf("Невозможно подключиться к базе данных. Код ошибки: %s\n", mysqli_connect_error()); 
   		exit; 
	?>
   </body>
</html>