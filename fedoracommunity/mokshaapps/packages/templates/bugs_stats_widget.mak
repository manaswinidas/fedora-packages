<div class="count-summary-dashboard">
  <div class="overlay"><div class="message"></div></div>
    <script type="text/javascript">
        function got_bug_stats(json) {
            $('#${id}_open_bugs').text(json.results.open);
            $('#${id}_num_new').text(json.results.new);
            $('#${id}_num_new_this_week').text(json.results.new_this_week + ' new this week.');
            $('#${id}_num_closed').text(json.results.closed);
            $('#${id}_num_closed_this_week').text(json.results.closed_this_week + ' closed this week.');
        }
        $(document).ready(function(){
            moksha.json_load('/moksha_connector/bugzilla/call/${filters}', {}, got_bug_stats, $(".count-summary-dashboard .overlay"));
        });
    </script>
    <dl class="count-box">
       <dt class="count-header main-count-header">Open Bugs</dt>
        <dd class="main-count-value" id="${id}_open_bugs">${num_open}</dd>
        <dd><span class="count-header">New</span> <span id="${id}_num_new">${num_new}</span></dd>
        <dd class="additional-info" colspan="2" id="${id}_num_new_this_week">${num_new_this_week}</dd>
    </dl>
    <dl class="count-box">
       <dt class="count-header main-count-header">Closed Bugs</th>
        <dd class="main-count-value" id="${id}_num_closed">${num_closed}</td>
        <dd class="additional-info" colspan="2" id="${id}_num_closed_this_week">${num_closed_this_week}</dd>
    </dl>
    <div class="action-box"><a class="action-header" href="https://bugzilla.redhat.com/enter_bug.cgi?product=${product}&version=${version}&component=${component}">Open A New Bug<br /> <img src="/images/action-box_add-button.png"></a>
    </div>
<div class="clear" />
</div>
