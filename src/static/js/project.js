/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');


$('#id_tripStart').datetimepicker({
    minDate: 0,
    format: 'Y-m-d H:i'
});

$('#id_property').select2({
    tags: true
});

$('#id_clients').select2();

    //
    // $(function () {
    //
    //     var options = {
    //         details: "#addNewAddress",
    //         detailsAttribute: "data-geo"
    //     }
    //     $("#id_address_input").geocomplete(options).bind('geocode:result', function (event, result) {
    //         $("#addressDate").removeClass('hidden');
    //         console.log(result);
    //         $.each(result.address_components, function (index, object) {
    //             var name = object.types[0];
    //             //console.log(name)
    //             var item = '';
    //             try {
    //                 item = $('input[data-geo=' + name + ']');
    //                 if (name == 'country' && $('select').attr('data-geo') == name) {
    //                     item = $('select[data-geo]');
    //                 }
    //                 if (item && item.attr('data-geo') == name) {
    //                     if (name == 'country') {
    //                         item.val(object.short_name)
    //                     }
    //                     else if (name == 'route') {
    //                         var string = $('#id_address_input').val()
    //                         var n = string.indexOf(result.name)
    //                         var apt = string.substring(0, n)
    //                         item.val(apt + " " + result.name)
    //                     }
    //                     else {
    //                         item.val(object.long_name);
    //                     }
    //                 }
    //             }
    //             catch (err) {
    //
    //             }
    //
    //         })
    //
    //
    //     });
    //
    //     $("#newAddressForm").on('submit', function (e) {
    //         e.preventDefault();
    //         $('#addAddress').children('.modal-content').toggleClass('sk-loading');
    //
    //
    //         var data = $(this).serialize();
    //         $.ajax({
    //             type: "POST",
    //             url: '/ajax/collectAddress/',
    //             data: data,
    //             success: function (data) {
    //                 console.log(data)
    //                 swal("Great!", "Address Saved!", "success")
    //                 $("#addAddress").modal('toggle');
    //
    //             }
    //
    //         });
    //
    //
    //     });
    //
    //
    //     $('.datepicker').datepicker();

    // });
