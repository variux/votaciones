jQuery(document).ready(function() {

    $(function() {

    //Switchery
        Switchery(document.querySelector('.js-switch-success'), {color: Utility.getBrandColor('success')});

    // EasyPieChart

        try {
            $('.easypiechart#progress').easyPieChart({
                barColor: "#cddc39",
                trackColor: 'rgba(255, 255, 255, 0.32)',
                scaleColor: false,
                scaleLength: 8,
                lineCap: 'square',
                lineWidth: 2,
                size: 96,
                onStep: function(from, to, percent) {
                    $(this.el).find('.percent-non').text(Math.round(percent));
                }
            });
        } catch(e) {}
    
    });

    

    //Loading Button in Timeline
    $('.loading-example-btn').click(function () {
        var btn = $(this)
        btn.button('loading')
        setTimeout(function () {
          btn.button('reset')
        },3000 )
    });


    // Visitor Stats
        function randValue() {
            return (Math.floor(Math.random() * (2)));
        }

        
        
    // Donut
        var datax = [
            { label: "Returning",  data: 68, color: '#7e57c2'},
            { label: "New",  data: 32, color: '#26c6da'}
        ];

      

});