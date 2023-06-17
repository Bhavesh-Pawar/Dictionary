$("#form").submit(function(event){
    event.preventDefault();
  });

function search_word(){
    let word = $('#word').val().trim();
    $.ajax({
        type : 'POST',
        url : '',
        data : {csrfmiddlewaretoken : csrf_token ,'action' : 'search_word' , 'word' : word},
        success : function (result) {
            console.log(result.data);
        }
    })
}