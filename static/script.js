// script.js
function search() {
    var genre = $("#genre_input").val();
    console.log("Genre:" + genre);

    $.ajax({
        url: `/search/${encodeURIComponent(genre)}`,
        method: "GET",
        dataType: "json",
        success: function(data) {
            $("#result_list").empty();
            for (var i = 0; i < data.length; i++) {
                $("#result_list").append("<li>" + data[i].Title + "</li>");
            }
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });
}