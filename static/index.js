const gaugeElement = document.querySelectorAll(".gauge");

function setGaugeValue(gauge, value) {
  if (value < 0 || value > 1) { return; }
  gauge.querySelector(".gauge__fill").style.transform = `rotate(${ value / 2 }turn)`;
  gauge.querySelector(".gauge__cover").textContent = `${Math.round( value * 100 )}%`;
}

function setGaugeValue1(gauge, value) {
  if (value < 0 || value > 1) { return; }
  gauge.querySelector(".gauge__fill").style.transform = `rotate(${ value / 2 }turn)`;
  gauge.querySelector(".gauge__cover").textContent = `${Math.round( value * 100 )}%`;
}

setGaugeValue(gaugeElement[0], ldr);
setGaugeValue1(gaugeElement[1], sm);

