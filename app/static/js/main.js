(function ($) {
	"use strict";


	// meanmenu with sidebar
	var win = $(window);
	$('#mobile-menu').meanmenu({
		meanMenuContainer: '.mobile-menu',
		meanScreenWidth: "991"
	});
	win.on('load', function () {
		$('#loading').hide();
	})
	$('.open-mobile-menu').on('click', function () {
		$('.side-info').addClass('info-open');
		$('.offcanvas-overlay').addClass('overlay-open');
	})

	$('.side-info-close,.offcanvas-overlay,.mobile_one_page li.menu-item a.nav-link').on('click', function () {
		$('.side-info').removeClass('info-open');
		$('.offcanvas-overlay').removeClass('overlay-open');
	})


	win.on('scroll', function () {
		var scroll = win.scrollTop();
		if (scroll < 245) {
			$(".header-sticky").removeClass("sticky");
		} else {
			$(".header-sticky").addClass("sticky");
		}
	});




	/*------------------------------------
		Slider
	--------------------------------------*/
	if ($(".slider-active").length > 0) {
		let sliderActive1 = '.slider-active';
		let sliderInit1 = new Swiper(sliderActive1, {
			// Optional parameters
			slidesPerView: 1,
			slidesPerColumn: 1,
			paginationClickable: true,
			loop: true,
			effect: 'fade',

			autoplay: {
				delay: 5000,
			},

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
				type: 'fraction',
				// clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.slide-next',
				prevEl: '.slide-prev',
			},

			a11y: false
		});

		function animated_swiper(selector, init) {
			let animated = function animated() {
				$(selector + ' [data-animation]').each(function () {
					let anim = $(this).data('animation');
					let delay = $(this).data('delay');
					let duration = $(this).data('duration');

					$(this).removeClass('anim' + anim)
						.addClass(anim + ' animated')
						.css({
							webkitAnimationDelay: delay,
							animationDelay: delay,
							webkitAnimationDuration: duration,
							animationDuration: duration
						})
						.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
							$(this).removeClass(anim + ' animated');
						});
				});
			};
			animated();
			// Make animated when slide change
			init.on('slideChange', function () {
				$(sliderActive1 + ' [data-animation]').removeClass('animated');
			});
			init.on('slideChange', animated);
		}

		animated_swiper(sliderActive1, sliderInit1);
	}
	// testimonial slider
	if ($(".testimonial-active").length > 0) {
		let swipertestimonial = new Swiper('.testimonial-active', {
			slidesPerView: 1,
			spaceBetween: 30,
			// direction: 'vertical',
			loop: true,
			infinite: false,
			autoplay: {
				delay: 5000,
			},

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
				clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.swiper-button-next',
				prevEl: '.swiper-button-prev',
			},

			// And if we need scrollbar
			scrollbar: {
				el: '.swiper-scrollbar',
				dynamicBullets: true,
			}

		});
	}
	// brand slider
	if ($(".brand-active").length > 0) {
		let swiperbrand = new Swiper('.brand-active', {
			slidesPerView: 5,
			spaceBetween: 30,
			// direction: 'vertical',
			loop: true,
			infinite: false,
			autoplay: {
				delay: 5000,
			},

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
				clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.swiper-button-next',
				prevEl: '.swiper-button-prev',
			},

			// And if we need scrollbar
			scrollbar: {
				el: '.swiper-scrollbar',
				dynamicBullets: true,
			},
			breakpoints: {
				320: {
					slidesPerView: 3,
				},
				480: {
					slidesPerView: 4,
				},
				768: {
					slidesPerView: 4,
				},
				1200: {
					slidesPerView: 5,
				},
				1400: {
					slidesPerView: 5,
				},
			}

		});
	}

	// news active
	if ($(".news-active-2").length > 0) {
		let swipernews = new Swiper('.news-active-2', {
			slidesPerView: 5,
			spaceBetween: 30,
			// direction: 'vertical',
			loop: true,
			infinite: false,
			autoplay: {
				delay: 5000,
			},

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
				clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.news-swiper-button-next',
				prevEl: '.news-swiper-button-prev',
			},

			// And if we need scrollbar
			scrollbar: {
				el: '.swiper-scrollbar',
				dynamicBullets: true,
			},
			breakpoints: {
				320: {
					slidesPerView: 1,
					spaceBetween: 0,
				},
				576: {
					slidesPerView: 2,
					spaceBetween: 10,
				},
				992: {
					slidesPerView: 3,
				},
				1200: {
					slidesPerView: 3,
				},
				1400: {
					slidesPerView: 4,
				},
			}

		});
	}
	// testtimonial active 2
	if ($(".testimonial-active-2").length > 0) {
		let swipertestimonial2 = new Swiper('.testimonial-active-2', {
			slidesPerView: 3,
			spaceBetween: 30,
			// direction: 'vertical',
			loop: true,
			infinite: false,
			autoplay: {
				delay: 5000,
			},

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
				clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.testi-swiper-button-next-2',
				prevEl: '.testi-swiper-button-prev-2',
			},

			// And if we need scrollbar
			scrollbar: {
				el: '.swiper-scrollbar',
				dynamicBullets: true,
			},
			breakpoints: {
				320: {
					slidesPerView: 1,
					spaceBetween: 0,
				},
				576: {
					slidesPerView: 1,
				},
				992: {
					slidesPerView: 3,
				},
				1200: {
					slidesPerView: 3,
				},
				1400: {
					slidesPerView: 3,
				},
			}

		});
	}
	// brand active 2
	if ($(".brand-active-2").length > 0) {
		let swiperbrand2 = new Swiper('.brand-active-2', {
			slidesPerView: 6,
			spaceBetween: 30,
			// direction: 'vertical',
			loop: true,
			infinite: false,
			autoplay: {
				delay: 5000,
			},

			// If we need pagination
			pagination: {
				el: '.swiper-pagination',
				clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.testi-swiper-button-next-2',
				prevEl: '.testi-swiper-button-prev-2',
			},

			// And if we need scrollbar
			scrollbar: {
				el: '.swiper-scrollbar',
				dynamicBullets: true,
			},
			breakpoints: {
				320: {
					slidesPerView: 2,
					spaceBetween: 0,
				},
				576: {
					slidesPerView: 4,
				},
				992: {
					slidesPerView: 5,
				},
				1200: {
					slidesPerView: 5,
				},
				1400: {
					slidesPerView: 6,
				},
			}

		});
	}
	// portfolio active
	if ($(".portfolio-swiper-active").length > 0) {
		let portfolioActive = new Swiper('.portfolio-swiper-active', {
			slidesPerView: 3,
			spaceBetween: 30,
			// direction: 'vertical',
			loop: true,
			infinite: false,
			autoplay: {
				delay: 5000,
			},

			// If we need pagination
			pagination: {
				el: '.swiper-portfolio-pagination',
				clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.portfolio-next',
				prevEl: '.portfolio-prev',
			},

			// And if we need scrollbar
			scrollbar: {
				el: '.swiper-scrollbar',
				dynamicBullets: true,
			},
			breakpoints: {
				320: {
					slidesPerView: 1,
					spaceBetween: 0,
				},
				576: {
					slidesPerView: 2,
				},
				992: {
					slidesPerView: 2,
				},
				1200: {
					slidesPerView: 3,
				},
				1400: {
					slidesPerView: 3,
				},
			}

		});
	}

	// data background
	$("[data-background]").each(function () {
		$(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
	})

	// data width
	$("[data-width]").each(function () {
		$(this).css("width", $(this).attr("data-width"))
	})
	// data width
	$("[data-color]").each(function () {
		$(this).css("color", $(this).attr("data-color"))
	})
	// data background color
	$("[data-bg-color]").each(function () {
		$(this).css("background-color", $(this).attr("data-bg-color"))
	})
	$('.sasup-accordion-item button.collapsed').parent().removeClass('sasup-disabled-item');
	$('.sasup-accordion-item button').on('click', function () {
		$('.sasup-accordion-item button').parent().addClass('sasup-active-item');
		$('.sasup-accordion-item button').parent().removeClass('sasup-disabled-item');
	})
	$('.sasup-accordion-item button.collapsed').on('click', function () {
		$('.sasup-accordion-item button.collapsed').parent().addClass('sasup-disabled-item');
		$('.sasup-accordion-item button.collapsed').parent().removeClass('sasup-active-item');
	})
	/* magnificPopup img view */
	$('.popup-image').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true
		}
	});

	/* magnificPopup video view */
	$('.popup-video-link').magnificPopup({
		type: 'iframe'
	});


	// scrollToTop
	$.scrollUp({
		scrollName: 'scrollUp', // Element ID
		topDistance: '300', // Distance from top before showing element (px)
		topSpeed: 300, // Speed back to top (ms)
		animation: 'fade', // Fade, slide, none
		animationInSpeed: 200, // Animation in speed (ms)
		animationOutSpeed: 200, // Animation out speed (ms)
		scrollText: '<i class="icofont icofont-long-arrow-up"></i>', // Text for element
		activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
	});

	// WOW active
	new WOW().init();

	// Active Odometer Counter 
	$('.odometer').appear(function (e) {
		var odo = $(".odometer");
		odo.each(function () {
			var countNumber = $(this).attr("data-count");
			$(this).html(countNumber);
		});
	});
	$(".sasup-hero-form").on('click', function () {
		$(".epix-hero-form-label").addClass('epix-hero-form-clicked');
	})
	// counterup
	$(".counter").counterUp({
		delay: 10,
		time: 2000,
	});
	$(".mobile-bar-control").on('click', function () {
		$(this).addClass('bar-control-clicked');
		$(".responsive-sidebar").addClass('responsive-sidebar-visible');
	});
	$(".responsive-sidebar-close").on("click", function () {
		$(".responsive-sidebar").removeClass("responsive-sidebar-visible");
		$(".mobile-bar-control").removeClass("bar-control-clicked");
	});
	$('.monthly-tab-btn').on('click', function () {
		$('.annual-tab-btn').addClass('pos-left-after');
	})
	$('.annual-tab-btn').on('click', function () {
		$('.annual-tab-btn').removeClass('pos-left-after');
	})
	// parallex
	if ($(".stuff").length) {
		var stuff = $('.stuff').get(0);
		var parallaxInstance = new Parallax(stuff);
	}
	if ($(".stuff2").length) {
		var stuff2 = $('.stuff2').get(0);
		var parallaxInstance = new Parallax(stuff2);
	}
	if ($(".stuff3").length) {
		var stuff3 = $('.stuff3').get(0);
		var parallaxInstance = new Parallax(stuff3);
	}
	if ($(".stuff4").length) {
		var stuff4 = $('.stuff4').get(0);
		var parallaxInstance = new Parallax(stuff4);
	}
	if ($(".stuff5").length) {
		var stuff5 = $('.stuff5').get(0);
		var parallaxInstance = new Parallax(stuff5);
	}
	if ($(".stuff6").length) {
		var stuff6 = $('.stuff6').get(0);
		var parallaxInstance = new Parallax(stuff6);
	}

	$("a.clickup").on('click', function (event) {
		if (this.hash !== "") {
			event.preventDefault();
			var hash = this.hash;
			$('html, body').animate({
				scrollTop: $(hash).offset().top
			}, 500, function () {
				window.location.hash = hash;
			});
		}
	});


	// isotop
	$('.portfolio-grid').imagesLoaded(function () {
		// init Isotope
		var $grid = $('.portfolio-grid').isotope({
			itemSelector: '.single-portfolio-filtered-item',
			percentPosition: true,
			masonry: {
				// use outer width of grid-sizer for columnWidth
				columnWidth: '.single-portfolio-filtered-item',
			}
		});
		// filter items on button click
		$('.portfolio-btn-group').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$grid.isotope({ filter: filterValue });
		});
		//for menu active class
		$('.portfolio-btn-group button').on('click', function (event) {
			$(this).siblings('.active').removeClass('active');
			$(this).addClass('active');
			event.preventDefault();
		});
	});


	//for menu active class
	$('.portfolio-menu button').on('click', function (event) {
		$(this).siblings('.active').removeClass('active');
		$(this).addClass('active');
		event.preventDefault();
	});
})(jQuery);