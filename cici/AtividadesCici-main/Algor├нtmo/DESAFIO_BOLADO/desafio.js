const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const linha = '-----------------------------------------------------------';
let sal_min, turno, categoria, horas_trab;

rl.question('Digite o salario minimo do funcionario: ', (answer) => {
  sal_min = parseFloat(answer);

  rl.question('-=-=-=-=-=-=-=-=-=-=-=-\n|   M - Matutino     |\n|   V - Vespertino   |\n|   N - Noturno      |\n-=-=-=-=-=-=-=-=-=-=-=-\n Digite a letra correspondente ao turno de trabalho: ', (answer) => {
    turno = answer.toUpperCase();

    rl.question('-=-=-=-=-=-=-=-=-=-=-=-\n|   O - Operario   |\n|   G - Gerente   |\n-=-=-=-=-=-=-=-=-=-=-=-\nDigite a letra correspondente à categoria do funcionário: ', (answer) => {
      categoria = answer.toUpperCase();

      rl.question('Digite o numero de horas trabalhadas no mes do funcionario: ', (answer) => {
        horas_trab = parseInt(answer);

        if (['M', 'V', 'N'].includes(turno) && ['O', 'G'].includes(categoria) && sal_min >= 0 && horas_trab >= 0) {
          let sal_bruto = 0;
          if (turno === 'M') {
            sal_bruto = (sal_min * 0.1) / horas_trab;
          } else if (turno === 'V') {
            sal_bruto = (sal_min * 0.15) / horas_trab;
          } else if (turno === 'N') {
            sal_bruto = (sal_min * 0.12) / horas_trab;
          }
          
          let imposto = 0;
          if (categoria === 'O' && sal_bruto >= 300) {
            imposto = sal_bruto * 0.05;
          } else if (categoria === 'O') {
            imposto = sal_bruto * 0.03;
          } else if (categoria === 'G' && sal_bruto >= 400) {
            imposto = sal_bruto * 0.06;
          } else {
            imposto = sal_bruto * 0.04;
          }
          
          console.log(`Salario bruto: R$ ${sal_bruto.toFixed(2)}`);
          console.log(`Imposto a ser pago: R$ ${imposto.toFixed(2)}`);
        } else {
          console.log('Valor invalido digitado!');
        }

        rl.close();
      });
    });
  });
});
