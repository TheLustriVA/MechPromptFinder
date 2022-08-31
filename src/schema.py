import json
from pprint import pprint

with open("metadata_example.json", "r", encoding="utf-8") as f:
    payload = json.load(f)
    
main_payload = payload['payload_docs']

ident_list = []
prompts_list = []
files_list = []
dimensions_list = []
colors_list = []
timings_list = []
losses_list = []
status_list = []
models_list = []
batch_list = []

for payload in main_payload:
    record_id = payload['uuid']
    
    ident_dict = {
        "record_id": record_id,
        "uuid": payload['uuid'],
        "$user_oid": payload['_id'].get('$oid'),
        "author_id": payload['author'],
        "agent_id": payload['agent_id']
    }
    
    ident_list.append(ident_dict)
    
    prompt_dict = {
        "record_id": record_id,
        "text_prompt": payload['text_prompt']
    }
    
    prompts_list.append(prompt_dict)
    
    files_dict = {
        "record_id": record_id,
        "filename": payload['filename'],
        "docarray": payload['discoart_tags'].get('name_docarray'),
        "picture": payload['userdets'].get('picture'),
        "jpg": payload['jpg']
    }
    
    files_list.append(files_dict)
    
    dimensions_dict = {
        "record_id": record_id,
        "width": payload['width_height'][0],
        "height": payload['width_height'][1],
        "thumbnail-sizes": payload['thumbnails'],
        "gif_size_ratio": payload['discoart_tags'].get('gif_size_ratio'),
        "gif_fps": payload['discoart_tags'].get('gif_fps')        
    }
    
    dimensions_list.append(dimensions_dict)
    
    color_dict = {
        "record_id": record_id,
        # dominant_color is a list of 3 values: [r, g, b]
        "dominant_color": payload['dominant_color'],
        # palette is a 2D, five-by-three list of [r, g, b] values
        "palette": payload['palette']
    }
    
    colors_list.append(color_dict)
    
    timing_dict = {
        "record_id": record_id,
        "timestamp": payload['timestamp'].get('$date'),
        "last_preview": payload['last_preview'].get('$date'),
        "time_completed": payload['time_completed'].get('$date'),
        "dt_timestamp": payload['dt_timestamp'].get('$date'),
        "str_timestamp": payload['str_timestamp'],
        "last_seen": payload['userdets'].get('last_seen').get('date')
    }
    
    timings_list.append(timing_dict)
    
    loss_dict = {
        "record_id": record_id,
        "loss_series": payload['discoart_tags'].get('_status').get('loss')
    }
    
    losses_list.append(loss_dict)
    
    status = {
        "record_id": record_id,
        "duration": payload['duration'],
        "percent": payload['percent'],
        "status": payload['discoart_tags'].get('_status'),
        "completed": payload['discoart_tags'].get('_status').get('completed'),
        "steps": payload['discoart_tags'].get('_status').get('step'),
        "cur_t": payload['discoart_tags'].get('_status').get('cur_t'),
        "stop_event": payload['discoart_tags'].get('stop_event'),
        "image_output": payload['discoart_tags'].get('image_output'),
        "results": payload['results']
    }
    
    status_list.append(status)
    
    models = {
        "record_id": record_id,
        "diffusion_model": payload['diffusion_model'],
        "clip_models": payload['clip_models'],
        "secondary_model": payload['use_secondary_model'],
        "diffusion_sampling_mode": payload['diffusion_sampling_mode'],
        "diffusion_model_config": payload['discoart_tags'].get('diffusion_model_config'),
        "clip_models_schedules": payload['discoart_tags'].get('clip_models_schedules'),
    }
    
    models_list.append(models)
    
    batch_details = {
        "record_id": record_id,
        "batch_size": payload['discoart_tags'].get('batch_size'),
        "n_batches": payload['discoart_tags'].get('n_batches'),
        "skip_event": payload['discoart_tags'].get('skip_event'),
        "use_vertical_symmetry": payload['discoart_tags'].get('use_vertical_symmetry'),
        "clip_denoised": payload['discoart_tags'].get('clip_denoised'),
        "sat_scale": payload['discoart_tags'].get('sat_scale'),
        "save_rate": payload['discoart_tags'].get('save_rate'),
        "visualize_cuts": payload['discoart_tags'].get('visualize_cuts'),
        "cut_overview": payload['discoart_tags'].get('cut_overview'),
        "clamp_grad": payload['discoart_tags'].get('clamp_grad'),
        "randomize_class": payload['discoart_tags'].get('randomize_class'),
        "clip_guidance_scale": payload['discoart_tags'].get('clip_guidance_scale'),
        "cut_schedules_group": payload['discoart_tags'].get('cut_schedules_group'),
        "cutn_batches": payload['discoart_tags'].get('cutn_batches'),
        "perlin_init": payload['discoart_tags'].get('perlin_init'),
        "range_scale": payload['discoart_tags'].get('range_scale'),
        "skip_steps": payload['discoart_tags'].get('skip_steps'),
        "init_image": payload['discoart_tags'].get('init_image'),
        "seed": payload['discoart_tags'].get('seed'),
        "on_misspelled_token": payload['discoart_tags'].get('on_misspelled_token'),
        "tv_scale": payload['discoart_tags'].get('tv_scale'),
        "text_clip_on_cpu": payload['discoart_tags'].get('text_clip_on_cpu'),
        "eta": payload['discoart_tags'].get('eta'),
        "use_horizontal_symmetry": payload['discoart_tags'].get('use_horizontal_symmetry'),
        "display_rate": payload['discoart_tags'].get('display_rate'),
        "init_scale": payload['discoart_tags'].get('init_scale'),
        "perlin_mode": payload['discoart_tags'].get('perlin_mode'),
        "cut_innercut": payload['discoart_tags'].get('cut_innercut'),
        "rand_mag": payload['discoart_tags'].get('rand_mag'),
        "steps": payload['discoart_tags'].get('steps'),
        "cut_icgray_p": payload['discoart_tags'].get('cut_icgray_p'),
        "cut_ic_pow": payload['discoart_tags'].get('cut_ic_pow'),
        "clamp_max": payload['discoart_tags'].get('clamp_max'),
        "truncate_overlength_prompt": payload['discoart_tags'].get('truncate_overlength_prompt'),
        "transformation_percent": payload['discoart_tags'].get('transformation_percent'),
        "batch_name": payload['discoart_tags'].get('batch_name')
    }
    
    batch_list.append(batch_details)
    

    
    def send_to_test_file():
        """
        Write a function that pretty-prints all the dictionaries in this file to a text file called dict_text.txt
        """
        with open('dict_text.txt', 'w') as f:
            json.dump(ident_list[0], f, indent=4)
            json.dump(prompts_list[0], f, indent=4)
            json.dump(files_list[0], f, indent=4)
            json.dump(dimensions_list[0], f, indent=4)
            json.dump(colors_list[0], f, indent=4)
            json.dump(timings_list[0], f, indent=4)
            json.dump(losses_list[0], f, indent=4)
            json.dump(status_list[0], f, indent=4)
            json.dump(models_list[0], f, indent=4)
            json.dump(batch_list[0], f, indent=4)
            
