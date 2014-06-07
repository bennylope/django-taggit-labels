// on click of a tag, it should be toggled - either added to or removed from an internal tracking
// array and its style changed.
//
// When the internal array changes, it should write out a new tag list to the hidden input

(function($) {
  $(document).ready(function() {
    // TODO this line assumes one tag field and that it is named as 'tags' -
    // this is too fragile
    var inputs = $("input#id_tags")[0];
    var tagItems = $("ul.tags li");
    var tagList = inputs.value.split(", ");
    tagItems.click(function() {
      var tagList = inputs.value.split(", ");
      var tagName = $(this).attr("data-tag-name");

      // Tag names need to be quotes if they contain commas or quotation marks
      if(tagName.indexOf(",") != -1 || tagName.indexOf(" ") != -1) {
        tagName = "\"" + tagName + "\"";
      }

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
})(django.jQuery);
