async function request_all_cupcakes() {
    const resp = await axios.get('api/cupcakes')
    const cupcakes = resp.data.cupcakes
    return cupcakes
}

async function load_cupcakes() {
    let cupcakes = await request_all_cupcakes();
    $('#cupcakes-list').empty();
    $('body').prepend("<h2 class='display-2 text-center'>Cupcakes!</h2>");
    for (let i = 0; i < cupcakes.length; i++) {
        html = `<li class='list-group-item'>
                    <img src=${cupcakes[i].image}>
                    <p>Flavor: ${cupcakes[i].flavor}</p>
                    <p>Size: ${cupcakes[i].size}</p>
                    <p>Rating: ${cupcakes[i].rating}</p>
                </li>`;
        $('#cupcakes-list').append(html);
    };
}

$(window).on("load", load_cupcakes)


async function add_cupcake() {
    const data = {
        "flavor": $("#flavor").val(),
        "size": $("#size").val(),
        "rating": $("#rating").val(),
        "image": $("#rating").val()
    }
    const res = await axios.post('api/cupcakes', data);
    load_cupcakes();
}

$('#cupcake-form').on('submit', function(e) {
    e.preventDefault();
    add_cupcake();
    
});
