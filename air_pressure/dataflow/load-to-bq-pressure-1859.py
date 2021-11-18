import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import logging

# defining Schema
schema_1859 = 'year:STRING, month:STRING, day:STRING, pressure_morning:STRING, thermometer_observations_1:STRING, air_pressure_reduced_to_0_degC_1:STRING, pressure_noon:STRING, thermometer_observations_2:STRING, air_pressure_reduced_to_0_degC_2:STRING, pressure_evening:STRING, thermometer_observations_3:STRING, air_pressure_reduced_to_0_degC_3:STRING'


class Split(beam.DoFn):
    def process(self, element):
        element = element.split(",")
        logging.info('Found : %s', element)
        return [{
            'year': element[0],
            'month': element[1],
            'day': element[2],
            'pressure_morning': element[3],
            'pressure_noon': element[4],
            'pressure_evening': element[5]
        }]


class BigQueryOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        # Use add_value_provider_argument for arguments to be templatable
        # Use add_argument as usual for non-templatable arguments
        parser.add_value_provider_argument('--input', help='Path of the file to read from')
        parser.add_value_provider_argument('--tableId', help='projectid:dataset.table')


def main():
    pipeline_options = PipelineOptions()
    big_query_options = pipeline_options.view_as(BigQueryOptions)

    with beam.Pipeline(options=PipelineOptions()) as p:
        (p
         | 'Read Data from GCS' >> beam.io.textio.ReadFromText(big_query_options.input)
         | 'Transformation' >> beam.ParDo(Split())
         | 'Write Data into BigQuery' >> beam.io.WriteToBigQuery(big_query_options.tableId, schema=schema_1859,
                                                                 write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
         )


if __name__ == '__main__':
    logger = logging.getLogger().setLevel(logging.INFO)
    main()
