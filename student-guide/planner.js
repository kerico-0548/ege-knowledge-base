'use strict';
const form = document.querySelector('#planner');
const output = document.querySelector('#budget');
const format = new Intl.NumberFormat('ru-RU', { maximumFractionDigits: 1 });
function updateBudget() {
  const controls = [...form.querySelectorAll('input')];
  if (controls.some(field => !field.validity.valid)) {
    output.textContent = 'Проверь поля. Нужны целые числа в указанном диапазоне.';
    return;
  }
  const [sessions, minutes, weeks] = controls.map(field => field.valueAsNumber);
  const weekly = sessions * minutes;
  output.textContent = format.format(weekly) + ' мин в неделю · ' + format.format(weekly * weeks / 60) + ' ч за весь период';
}
form.addEventListener('input', updateBudget);
form.addEventListener('submit', event => event.preventDefault());
updateBudget();
