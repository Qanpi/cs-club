donationCounter = document.getElementById("counter");
count = 0;

function handleDonation() {
  count++;
  donationCounter.innerText = "Donations so far: " + count;
}
