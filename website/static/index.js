function deleteCar(carId) {
  fetch("/delete-car", {
    method: "POST",
    body: JSON.stringify({ carId: carId }),
  }).then((_res) => {
    window.location.href = "/removercarro";
  });
}