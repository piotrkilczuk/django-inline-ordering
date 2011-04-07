var InlineOrdering = {

    /**
     * Get list of elements that can be reordered
     *
     * At this point, only already existent records can be reordered (ie. where pk != '')
     *
     * @return Array
     * @todo Check if given record changed, and if so, make it reorderable
     * @todo Primary key might not be 'id' - better selector needed
     *
     */
    getOrderables: function(){
        var allInlineRows = jQuery('.inline-related');
        var ids = [];
        
        for (var i = 0; i < allInlineRows.length; i++) {
            if (jQuery('.inline_ordering_position input', allInlineRows[i]).val()) {
                ids.push('#' + allInlineRows[i].id);
            }
        }
        
        // this redundant way is required, so that proper order is maintained, 
        // otherwise orderables were returned in more or less random order 	
        return jQuery(ids.join(', ')); 
    },
    
    /**
     * Inits the jQuery UI D&D
     *
     */
    init: function(){
        jQuery("div.inline-group").sortable({
            axis: 'y',
            placeholder: 'ui-state-highlight',
            forcePlaceholderSize: 'true',
            items: InlineOrdering.getOrderables(),
            update: InlineOrdering.update
        });
        //jQuery("div.inline-group").disableSelection();
        
        jQuery('div.inline_ordering_position').hide();
        jQuery('td.inline_ordering_position input').hide();
        
        jQuery('.add-row a').click(InlineOrdering.update);
		
		InlineOrdering.getOrderables().css('cursor', 'move');
    },
    
    /**
     * Updates the position field
     *
     */
    update: function(){
        InlineOrdering.getOrderables().each(function(i){
            jQuery(this).find('input[id$=inline_ordering_position]').val(i + 1);
        });
    }
    
};

jQuery(function(){
    InlineOrdering.init();
});
