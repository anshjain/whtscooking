 $(document).ready(function() {
     $('.combobox').combobox();
     $("#id_vendor_rating").rating({min:1, max:10, step:2, size:'lg'});
     $("#id_vendor_overall_rating").rating({displayOnly: true, size:'sm'});
 });
