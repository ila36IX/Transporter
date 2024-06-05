$(document).ready(function () {
    const customerData = [
        {
            company: "Alex",
            type: "Onion",
            weight: "35ton",
            location: "Rabat",
            price: "200$"
        },
        {
            company: "Example Corp",
            type: "Apples",
            weight: "20ton",
            location: "Casablanca",
            price: "150$"
        },
        {
            company: "Fruit Co",
            type: "Bananas",
            weight: "40ton",
            location: "Marrakech",
            price: "400$"
        },
        {
            company: "Atlas",
            type: "water",
            weight: "40ton",
            location: "Marrakech",
            price: "300$"
        }
    ];

    function populateCustomerCards(dataArray) {
        const container = $('#card-cust'); // Select the container for the cards
        container.empty(); // Clear the container

        dataArray.forEach((customer) => {
            const card = $('<div>').addClass('cards'); // Create card container
            const cardContent = $('<div>').addClass('card-content').appendTo(card); // Create and append card content container
            $('<h2>').addClass('card-title').text('Customer Profile').appendTo(cardContent); // Add card title
            
            const customerInfo = $('<div>').addClass('Customer-info').appendTo(cardContent); // Create and append customer info container

            // Populate customer info
            $('<div>').addClass('company-name')
                      .append($('<h2>').text('Company Name:'))
                      .append($('<p>').addClass('company').text(customer.company))
                      .appendTo(customerInfo);
            
            $('<div>').addClass('cargo-type')
                      .append($('<h2>').text('Cargo type:'))
                      .append($('<p>').addClass('type').text(customer.type))
                      .appendTo(customerInfo);

            $('<div>').addClass('cargo-weight')
                      .append($('<h2>').text('Cargo weight:'))
                      .append($('<p>').addClass('weight').text(customer.weight))
                      .appendTo(customerInfo);

            $('<div>').addClass('company-location')
                      .append($('<h2>').text('Location:'))
                      .append($('<p>').addClass('location').text(customer.location))
                      .appendTo(customerInfo);

            $('<div>').addClass('cargo-price')
                      .append($('<h2>').text('Price:'))
                      .append($('<p>').addClass('price').text(customer.price))
                      .appendTo(customerInfo);

            container.append(card); // Append the populated card to the container
        });
    }

    // Call the function with the sample data
    populateCustomerCards(customerData);
});
