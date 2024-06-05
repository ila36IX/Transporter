$(document).ready(function() {
  const driverData = [
      { name: "John Doe", truck: "Truck A", license: "ABC123", location: "Rabat", delivered: true, rating: 5 },
      { name: "Jane Smith", truck: "Truck B", license: "XYZ789", location: "Marakech", delivered: false, rating: 3 },
      { name: "Jane Smith", truck: "Truck B", license: "XYZ789", location: "Casablanca", delivered: false, rating: 3 },
      { name: "Jane Smith", truck: "Truck B", license: "XYZ789", location: "Beni mellal", delivered: false, rating: 3 },
      { name: "Jane Smith", truck: "Truck B", license: "XYZ789", location: "Meknas", delivered: false, rating: 3},
      { name: "Jane Smith", truck: "Truck B", license: "XYZ789", location: "Azilal", delivered: false, rating: 3 },
  ];

  const uniqueCities = [...new Set(driverData.map(driver => driver.location))];

  function filterCities(query) {
      return uniqueCities.filter(city => city.toLowerCase().startsWith(query.toLowerCase()));
  }

  function displaySuggestions(inputElement, suggestionsContainer, filteredCities) {
      suggestionsContainer.empty();
      if (filteredCities.length > 0) {
          filteredCities.forEach(city => {
              const suggestionItem = $('<div>').addClass('suggestion-item').text(city);
              suggestionItem.on('click', function() {
                  inputElement.val(city);
                  suggestionsContainer.empty().hide();
              });
              suggestionsContainer.append(suggestionItem);
          });
          suggestionsContainer.show();
      } else {
          suggestionsContainer.hide();
      }
  }

  $('.searchInput').on('focus', function() {
      displaySuggestions($(this), $('#current-city-suggestions'), uniqueCities);
  });

  $('.searchInput1').on('focus', function() {
      displaySuggestions($(this), $('#destination-suggestions'), uniqueCities);
  });

  $('.searchInput').on('input', function() {
      const query = $(this).val();
      const filteredCities = filterCities(query);
      displaySuggestions($(this), $('#current-city-suggestions'), filteredCities);
  });

  $('.searchInput1').on('input', function() {
      const query = $(this).val();
      const filteredCities = filterCities(query);
      displaySuggestions($(this), $('#destination-suggestions'), filteredCities);
  });

  $(document).on('click', function(e) {
      if (!$(e.target).closest('.searchBox').length) {
          $('.suggestions').hide();
      }
  });
});
