/* ============================================
   Selling 303 — Main JavaScript
   ============================================ */

(function () {
  'use strict';

  // --- Mobile Navigation ---
  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('nav');
  const navOverlay = document.getElementById('navOverlay');

  if (hamburger && nav) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      nav.classList.toggle('active');
      if (navOverlay) navOverlay.classList.toggle('active');
      document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
    });

    if (navOverlay) {
      navOverlay.addEventListener('click', function () {
        hamburger.classList.remove('active');
        nav.classList.remove('active');
        navOverlay.classList.remove('active');
        document.body.style.overflow = '';
        // Close all dropdowns
        document.querySelectorAll('.has-dropdown.dropdown-open').forEach(function (d) {
          d.classList.remove('dropdown-open');
          var btn = d.querySelector('.dropdown-toggle');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        });
      });
    }

    // Close nav on dropdown item click (mobile)
    nav.querySelectorAll('.dropdown-item').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        nav.classList.remove('active');
        if (navOverlay) navOverlay.classList.remove('active');
        document.body.style.overflow = '';
      });
    });
  }

  // --- Dropdown Navigation ---
  var dropdownToggles = document.querySelectorAll('.dropdown-toggle');

  dropdownToggles.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var parent = btn.closest('.has-dropdown');
      var isOpen = parent.classList.contains('dropdown-open');

      // Close all open dropdowns
      document.querySelectorAll('.has-dropdown.dropdown-open').forEach(function (d) {
        d.classList.remove('dropdown-open');
        var b = d.querySelector('.dropdown-toggle');
        if (b) b.setAttribute('aria-expanded', 'false');
      });

      // Toggle this one (if it wasn't already open)
      if (!isOpen) {
        parent.classList.add('dropdown-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // Close dropdowns on outside click (desktop)
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-dropdown')) {
      document.querySelectorAll('.has-dropdown.dropdown-open').forEach(function (d) {
        d.classList.remove('dropdown-open');
        var btn = d.querySelector('.dropdown-toggle');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Close dropdowns on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.has-dropdown.dropdown-open').forEach(function (d) {
        d.classList.remove('dropdown-open');
        var btn = d.querySelector('.dropdown-toggle');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // --- Sticky Header (scroll behavior) ---
  var header = document.getElementById('header');

  if (header && !header.classList.contains('header--solid')) {
    var scrollThreshold = 60;

    function handleScroll() {
      if (window.scrollY > scrollThreshold) {
        header.classList.add('header--scrolled');
      } else {
        header.classList.remove('header--scrolled');
      }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Initial check
  }

  // --- Smooth Scroll for Anchor Links ---
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var headerHeight = header ? header.offsetHeight : 80;
        var targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // --- Blog Filter Buttons (UI only — functional with CMS integration) ---
  var filterButtons = document.querySelectorAll('.blog-filter');
  if (filterButtons.length > 0) {
    filterButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filterButtons.forEach(function (b) { b.classList.remove('blog-filter--active'); });
        this.classList.add('blog-filter--active');
        // Filter logic would connect to CMS/static site generator
      });
    });
  }

})();
