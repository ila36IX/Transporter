$(document).ready(function () {
  const driverData = [
      {
          name: "Mohamed",
          truck: "Volvo",
          license: "AB",
          location: "BM",
          delivered: false,
          rating: 3
      },
      {
          name: "Abdos",
          truck: "Scania",
          license: "AB",
          location: "BM",
          delivered: false,
          rating: 4
      },
      {
        name: "Hassna",
        truck: "Mercedes",
        license: "AB",
        location: "BM",
        delivered: false,
        rating: 4
    },
    {
      name: "ayoub",
      truck: "Volvo",
      license: "AB",
      location: "agadir",
      delivered: true,
      rating: 3
  },
  {
    name: "Amal",
    truck: "Scania",
    license: "AB",
    location: "casa",
    delivered: false,
    rating: 2
}
  ];


  const randomImageUrl = "https://100k-faces.glitch.me/random-image";

  // Function to populate driver cards
  function populateDriverCards(dataArray) {
      const container = $('#cards-container');  // Select the container for the cards
      const templateCard = $('.card').first().clone().removeAttr('style');  // Clone the hidden template card and make it visible

      container.empty();  // Clear the container

      dataArray.forEach((driver, index) => {
          const newCard = templateCard.clone();  // Clone the template for each driver

          // Populate the cloned card with driver data
          newCard.find('.driver-name-text').text(driver.name);
          newCard.find('.driver-truck-text').text(driver.truck);
          newCard.find('.driver-license-text').text(driver.license);
          newCard.find('.driver-location-text').text(driver.location);

          // Assign the random image URL to the avatar
          const avatarImage = newCard.find('.avatar img');
          avatarImage.attr('src', randomImageUrl + "?cache=" + new Date().getTime()); // Ensure a fresh image each time by adding a cache-busting query parameter

          // Ensure the delivered checkbox is unique
          const deliveredCheckbox = newCard.find('.delivered-checkbox');
          deliveredCheckbox.prop('checked', driver.delivered);
          const deliveredCheckboxId = 'delivered-' + index;
          deliveredCheckbox.attr('id', deliveredCheckboxId);
          newCard.find('label[for="one"]').attr('for', deliveredCheckboxId);

          // Set rating stars
          newCard.find('.star-radio').each(function (i) {
              $(this).prop('checked', (i + 1) === driver.rating);
              const starId = 'star-' + (i + 1) + '-' + index;  // Ensure unique id for each driver's stars
              $(this).attr('name', 'star-radio-' + index);  // Ensure unique name for each driver's stars
              $(this).attr('id', starId);  // Set unique id
              $(this).next('label').attr('for', starId);  // Ensure the label points to the correct star
          });

          container.append(newCard);  // Append the populated card to the container
      });
  }

  // Call the function with the sample data
  populateDriverCards(driverData);
});
