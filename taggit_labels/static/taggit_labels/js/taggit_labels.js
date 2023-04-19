// on click of a tag, it should be toggled - either added to or removed from an internal tracking
// array and its style changed.
//
// When the internal array changes, it should write out a new tag list to the hidden input

(function($) {
    $(document).ready(function() {
        $(".taggit-labels").closest("div").each(function(i) {
            var inputs = $(this).find(".taggit-labels + input")[0];
            var tagItems = $(this).find(".taggit-list .taggit-tag");
            var tagList = inputs.value.split(", ");
            tagItems.click(function() {
                // split input value in array by ", " but ignore a comma between double quotes
                var tagList = inputs.value.match(/(?:[^, "]+|"[^"]*")+/g);
                if (!tagList) tagList = [];
                // Always wrap tag name with double quote
                var tagName = "\"" + $(this).attr("data-tag-name") + "\"";

                var index = $.inArray(tagName, tagList);
                // Add the selected tag to the list of tags if it wasn't there previously
                // and remove it if it was present.
                if(index == -1) {
                    $(this).toggleClass("selected");
                    tagList.push(tagName);
                } else {
                     $(this).toggleClass("selected");
                     tagList.splice(index, 1);
                }

                // Refresh the tag list
                $(inputs).attr("value", tagList.join(", "));
            });
        });
    });
})(jQuery || django.jQuery);
