$("#selectFile").bind('change',function(){
    var filename = $("#selectFile").val();
    if(/^s*$/.test(filename)){
        $("#blankFile").text("No File Chosen..");
        $(".success").hide();
    }else{
        $("#blankFile").text(filename.replace("C:\\fakepath\\",""));
        $(".success").show();
    }
}) 

// Feedback
/*Dropdown Menu*/
$('.dropdown').click(function () {
    $(this).attr('tabindex', 1).focus();
    $(this).toggleClass('active');
    $(this).find('.dropdown-menu').slideToggle(300);
});
$('.dropdown').focusout(function () {
    $(this).removeClass('active');
    $(this).find('.dropdown-menu').slideUp(300);
});
$('.dropdown .dropdown-menu li').click(function () {
    $(this).parents('.dropdown').find('span').text($(this).text());
    $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
});
/*End Dropdown Menu*/


/* Upload and cancel button hover */
document.getElementById('upload').addEventListener('mouseover', function () {
    const cancel = document.getElementById('cancel');
    const upload = document.getElementById('upload');
    upload.style.backgroundColor = "var(--primary)";
    cancel.style.backgroundColor = "";
    cancel.style.color = "var(--secondary)";
    upload.style.color = "var(--background)";
    upload.style.transition="0.3s all"
})
document.getElementById('cancel').addEventListener('mouseover', function () {
    const cancel = document.getElementById('cancel');
    const upload = document.getElementById('upload');
    cancel.style.backgroundColor = "var(--primary)";
    upload.style.backgroundColor = "transparent";
    upload.style.color = "var(--secondary)"
    cancel.style.color = "var(--background)"
    upload.style.transition="0.3s all"
})