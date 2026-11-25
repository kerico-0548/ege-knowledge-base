(() => {
  const root = document.documentElement;
  const key = "kerico-reading-theme";
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  let selected;
  try { selected = localStorage.getItem(key); } catch {}
  function apply() {
    const dark = selected === "dark" || (selected !== "light" && system.matches);
    root.dataset.theme = dark ? "dark" : "light";
    const button = document.querySelector(".theme");
    if (!button) return;
    button.hidden = false;
    button.querySelector(".mode-icon").textContent = dark ? "☀" : "☾";
    button.querySelector(".mode-label").textContent = dark ? "Светлый фон" : "Тёмный фон";
    button.setAttribute("aria-label", dark ? "Включить светлый фон" : "Включить тёмный фон");
  }
  apply();
  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".theme");
    apply();
    button.addEventListener("click", () => {
      selected = root.dataset.theme === "dark" ? "light" : "dark";
      try { localStorage.setItem(key, selected); } catch {}
      apply();
    });
  });
  if (system.addEventListener) system.addEventListener("change", apply);
  window.addEventListener("storage", event => {
    if (event.key === key || event.key === null) { selected = event.newValue; apply(); }
  });
})();
