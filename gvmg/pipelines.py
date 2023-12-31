# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from datetime import datetime
import re


class GvmgPipeline:
    def process_item(self, item, spider):        
        adapter = ItemAdapter(item)

        ## Date: "Lahatrsoratra tamin'ny YYYY/mm/dd" format to "dd/mm/YYYY"
        date_value = adapter.get('date')        
        if isinstance(date_value, tuple): # tuple to string
            date_value = ' '.join(date_value)      
        if isinstance(date_value, str): # is a string ?
            match = re.search(r'\d{4}/\d{2}/\d{2}', date_value)
            if match:
                cleaned_date = match.group()  # Extract the date
                try:
                    date_object = datetime.strptime(cleaned_date, '%Y/%m/%d')
                    formatted_date = date_object.strftime('%d/%m/%Y')
                    adapter['date'] = formatted_date  # Update with the new date format
                except ValueError:
                    pass


        ## Convert place_value "(None,)" for ""
        place_value = adapter.get('place')
        if isinstance(place_value, tuple) and len(place_value) == 1 and place_value[0] is None:
            adapter['place'] = ""  # Update with an empty string


        return item
