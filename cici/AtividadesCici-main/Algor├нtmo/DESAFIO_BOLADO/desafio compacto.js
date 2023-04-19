const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

let sal_min, turno, categoria, horas_trab;

readline.question('Digite o salario minimo do funcionario: ', (answer) => (
  sal_min = parseFloat(answer),
  readline.question('-=-=-=-=-=-=-=-=-=-=-=-\n|   M - Matutino     |\n|   V - Vespertino   |\n|   N - Noturno      |\n-=-=-=-=-=-=-=-=-=-=-=-\n Digite a letra correspondente ao turno de trabalho: ', (answer) => (
    turno = answer.toUpperCase(),
    readline.question('-=-=-=-=-=-=-=-=-=-=-=-\n|   O - Operario   |\n|   G - Gerente   |\n-=-=-=-=-=-=-=-=-=-=-=-\nDigite a letra correspondente à categoria do funcionário: ', (answer) => (
      categoria = answer.toUpperCase(),
      readline.question('Digite o numero de horas trabalhadas no mes do funcionario: ', (answer) => (
        horas_trab = parseInt(answer),
        ['M', 'V', 'N'].includes(turno) && ['O', 'G'].includes(categoria) && sal_min >= 0 && horas_trab >= 0 ? (
          sal_bruto = (turno === 'M' ? sal_min * 0.1 : turno === 'V' ? sal_min * 0.15 : sal_min * 0.12) / horas_trab,
          imposto = (categoria === 'O' && sal_bruto >= 300 ? sal_bruto * 0.05 : categoria === 'O' ? sal_bruto * 0.03 : categoria === 'G' && sal_bruto >= 400 ? sal_bruto * 0.06 : sal_bruto * 0.04),
          console.log(`Salario bruto: R$ ${sal_bruto.toFixed(2)}`),
          console.log(`Imposto a ser pago: R$ ${imposto.toFixed(2)}`)
        ) : console.log('Valor invalido digitado!'),
        readline.close()
      ))
    ))
  ))
));
