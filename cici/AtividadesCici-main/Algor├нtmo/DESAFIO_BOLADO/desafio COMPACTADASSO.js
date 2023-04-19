const readline = require('readline').createInterface({input: process.stdin, output: process.stdout});

const ask = async (prompt) => new Promise((resolve) => readline.question(prompt, resolve));

const sal_min = parseFloat(await ask('Digite o salario minimo do funcionario: '));
const turno = (await ask(`-=-=-=-=-=-=-=-=-=-=-=-\n|   M - Matutino     |\n|   V - Vespertino   |\n|   N - Noturno      |\n-=-=-=-=-=-=-=-=-=-=-=-\nDigite a letra correspondente ao turno de trabalho: `)).toUpperCase() ?? '';
const categoria = (await ask(`-=-=-=-=-=-=-=-=-=-=-=-\n|   O - Operario   |\n|   G - Gerente   |\n-=-=-=-=-=-=-=-=-=-=-=-\nDigite a letra correspondente à categoria do funcionário: `)).toUpperCase() ?? '';
const horas_trab = parseInt(await ask('Digite o numero de horas trabalhadas no mes do funcionario: '));

if (['M', 'V', 'N'].includes(turno) && ['O', 'G'].includes(categoria) && sal_min >= 0 && horas_trab >= 0) {
  const sal_bruto = (turno === 'M' ? sal_min * 0.1 : turno === 'V' ? sal_min * 0.15 : sal_min * 0.12) / horas_trab;
  const imposto = (categoria === 'O' && sal_bruto >= 300 ? sal_bruto * 0.05 : categoria === 'O' ? sal_bruto * 0.03 : categoria === 'G' && sal_bruto >= 400 ? sal_bruto * 0.06 : sal_bruto * 0.04);

  console.log(`Salario bruto: R$ ${sal_bruto.toFixed(2)}`);
  console.log(`Imposto a ser pago: R$ ${imposto.toFixed(2)}`);
} else {
  console.log('Valor invalido digitado!');
}

readline.close();
