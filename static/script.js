function search() {
    var genre = $("#genre_input").val();
    console.log("Genre:" + genre);

    $.ajax({
        url: `/search/${encodeURIComponent(genre)}`,
        method: "GET",
        dataType: "json",
        success: function (data) {
            $("#result_list").empty();       // Clear previous results
            $("#message").text("");           // Clear previous message

            if (data.length === 0) {
                // Show message instead of list item
                $("#message").text("There is no book with this genre, please try something else");
            } else {
                // Populate list as usual
                for(var i = 0; i < data.length; i++) {
                    $("#result_list").append("<li>" + data[i].Title + "</li>");
                }
            }
        },
        error: function (xhr, status, error) {
            console.error("Error:", error);
        }
    });
}