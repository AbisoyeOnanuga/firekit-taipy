# **Wildfire Status**{: .color-primary} Alerts

<|{selected_location}|selector|lov={selector_location}|on_change=on_change_location|dropdown|label=Location|>

<br/>

<|layout|columns=1 1 1|gap=50px|
<|card|
**Location**{: .color-primary}
<|{data_location.iloc[-1]['Location']}|text|class_name=h2|>
|>

<|card|
**Stage of Control**{: .color-primary}
<|{data_location.iloc[-1]['Stage of Control']}|text|class_name=h2|>
|>

<|card|
**Estimated Size (Ha)**{: .color-primary}
<|{'{:,}'.format(int(data_location.iloc[-1]['Estimated Size (Ha)'])).replace(',', ' ')}|text|class_name=h2|>
|>
|>
<br/>
<br/>
<|layout|columns=1 1 1|gap=50px|
<|card|
**Fire Centre**{: .color-primary}
<|{data_location.iloc[-1]['Fire Centre']}|text|class_name=h2|>
|>

<|card|
**Last Updated**{: .color-primary}
<|{data_location.iloc[-1]['Last Updated']}|text|class_name=h2|>
|>

<|card|
**Discovery Date**{: .color-primary}
<|{data_location.iloc[-1]['Discovery Date']}|text|class_name=h2|>
|>
|>