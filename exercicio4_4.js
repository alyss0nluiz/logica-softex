const mysql = require('mysql2');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'username',
  password: 'password',
  database: 'database'
});

connection.connect((err) => {
  if (err) {
    console.log(`Erro ao conectar ao banco de dados: ${err.message}`);
  } else {
    console.log("Conexão com o banco de dados estabelecida com sucesso!");
  }
});
