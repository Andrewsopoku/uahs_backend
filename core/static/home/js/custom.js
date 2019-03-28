// Animations init
     new WOW().init();
	 
	 $('#others').material_chip({
    placeholder:'Add Disease.',
    secondaryPlaceholder: 'Add Disease And Press Enter.',
});

$('#currentmed').material_chip({
    placeholder:'Add Medication-Dosage-Time.',
    secondaryPlaceholder:'Add Medication - Dosage - Time .',
});

$('#surgeries').material_chip({
    placeholder:'Add Surgery - Date',
    secondaryPlaceholder:'Add (Surgery - Date).',
});

var data= $('#others').material_chip('data');
alert(data[0].tag);

var data= $('#currentmed').material_chip('data');
alert(data[0].tag);

var data= $('#surgeries').material_chip('data');
alert(data[0].tag);

