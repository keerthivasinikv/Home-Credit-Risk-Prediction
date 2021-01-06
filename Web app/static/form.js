$('#predict').on('submit', function(e){
        e.preventDefault();
        var formData = new FormData();
        formData.append('file', $('#file_demo')[0].files[0]);
        console.log(formData);

        $.ajax({
            type: "POST",
            url: "/predict",
            data : formData,
            processData: false,  // tell jQuery not to process the data
            contentType: false,  // tell jQuery not to set contentType
            success: function(response_data) {
                console.log(response_data.prediction);
            $('#download_file').attr('href', response_data.prediction)
            $('#download_file')[0].click();
            },
            error: function() {}
        })
    })