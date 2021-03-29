let operacion = '';
const updateResult = (text = '') => {
    const input = $('#input');
    const result = input.val() + text;
    input.val(result);
};
const bloquear = (disabled = true) => {
    const buttons = $('.operador').toArray();
    buttons.forEach( button => {
        button.disabled = disabled;
    });
};
const operador = (button) => {
    const value = button.value;
    bloquear();
    updateResult(' ' + value + ' ');
    if (value === '+') {
        operacion = 'suma';
    } else if (value === '-') {
        operacion = 'resta';
    } else if (value === '*') {
        operacion = 'multiplicacion';
    } else if (value === '/') {
        operacion = 'division';
    }
};
const limpiar = () => {
    $('#input').val('');
    operacion = '';
    bloquear(false);
}
const numero = (button) => {
    updateResult(button.value);
};
const submit = () => {
    const input = $('#input');
    const numeros = input.val().split(' ');
    const url = 'http://127.0.0.1:5000/operacion?' + 'operador='+operacion + '&valor_1=' + numeros[0] + '&valor_2=' + numeros[2];
    const form = $('#form').get(0);
    form.action = url;
    form.submit();
}
$(document).ready(function () {
    $('.operador').on('click', $event => {
        operador($event.target);
    });
    $('.numero').on('click', $event => {
        numero($event.target);
    });
    $('#limpiador').on('click', () => {
        limpiar();
    });
    $('#enviar').on('click', () => {
        submit();
    });
});