$(document).ready(function(){

    $("#downloadDocument").click(function(){
        var serializedData = 
        $("#downloadDocumentForm").serialize();
        var filePath = $("#file_path").val()
        let fileName = filePath.split('/').pop()
        console.log(filePath)
        $.ajax({
          type: 'post',
          url: "/download_document",
          data: serializedData,
          dataType: "html",
          success: function (response) {
            var blob = new Blob([response], {type: 'application/x-download'});
            var downloadUrl = URL.createObjectURL(blob);
            var a = document.createElement("a");
            a.href = downloadUrl;
            a.download = fileName;
            document.body.appendChild(a);
            a.click();
          },
          error : function(xhr,errmsg,err) {
            alert('Error:' + errmsg)
          }
        });
    })
})