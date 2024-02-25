# maddata-backend
Backend for maddata group with DK Kim, Colin Luangrath, Alex Ge, and Vince Cimino
##Inspiration
We were captivated by the extensive and insightful dataset available at https://www.kaggle.com/datasets/mvieira101/global-cost-of-living, which led us to further enrich this data by incorporating additional datasets from https://www.kaggle.com/datasets/paultimothymooney/the-economists-big-mac-index and https://www.kaggle.com/datasets/alejopaullier/-gdp-by-country-1999-2022. Our ambition was to not only visualize the average data values for each country globally but also to delve into the variations present within individual cities, offering a more granular view of the cost of living landscape.

##What it does
PriceSlice presents a comprehensive global map, designed with interactivity at its core, allowing users to select various data points to unveil detailed displays of values by country and city. This dynamic visualization serves as a global lens, offering insights into the cost of living, economic health, and purchasing power parity across different regions.

##How we built it
We leveraged the robustness of React.js for the frontend to create a responsive and intuitive user interface. The backend, powered by Flask, serves as a REST API, meticulously designed to handle data processing, aggregation, and response to frontend requests. This bifurcated approach allowed us to develop a scalable, efficient, and user-friendly platform that bridges complex datasets with interactive visualizations.

##Challenges we ran into
One of the significant challenges we faced was ensuring seamless integration and harmonization of data from diverse sources, each with its unique structure and metrics. Additionally, optimizing the performance of the interactive global map to handle large datasets without compromising on user experience posed a considerable technical hurdle.

##Accomplishments that we're proud of
We are particularly proud of our ability to create a cohesive and engaging user experience that simplifies the complexity of global economic data. The development of an efficient backend that swiftly processes and delivers data to the frontend, enabling real-time interactivity on the global map, stands as a testament to our team's technical prowess.

##What we learned
Throughout this project, we gained invaluable insights into data integration, the nuances of building scalable REST APIs, and the intricacies of frontend development with React.js. The challenge of visualizing complex data in an accessible manner also honed our skills in UI/UX design.

##What's next for PriceSlice
Moving forward, PriceSlice aims to incorporate real-time economic indicators and forecasts to provide even more dynamic and predictive insights. We also plan to enhance the platform's interactivity by introducing comparative analysis features, enabling users to juxtapose different data points and derive comprehensive insights into global economic trends.
