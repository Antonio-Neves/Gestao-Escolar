// Masks
$(document).ready(function(){
  $('#aluno_cpf').mask('000.000.000-00');
  $('#aluno_filiacao1_cpf').mask('000.000.000-00');
  $('#aluno_filiacao2_cpf').mask('000.000.000-00');
});

$(document).ready(function(){
  $('#aluno_certidao_nova').mask('000000 00 00 0000 0 00000 000 0000000 00');
});

$(document).ready(function(){
  $('#aluno_cep_residencia').mask('00000-000');
});

$(document).ready(function(){
  $('#aluno_data_nascimento').mask('00/00/0000');
});
// Select2
// $(document).ready(function() {
//     $('#aluno_municipio_nascimento').select2();
// });
//
// $(document).ready(function() {
//     $('#aluno_municipio_residencia').select2();
// });



// $(document).ready(function () {
//     $('#id_aluno_municipio_nascimento').select2({
//         ajax: {
//             url: "{% url 'formulario' %}",
//             dataType: 'json',
//             processResults: function (data) {
//                 return {
//                     results: $.map(data, function (item) {
//                         return {id: item.id, text: item.title};
//                     })
//                 };
//             }
//         },
//         minimumInputLength: 1
//     });
// });
