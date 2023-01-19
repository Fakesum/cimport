#[no_mangle]
fn return_int()->i32{ return 1 }

#[no_mangle]
fn return_float() -> f32{ return 1.0; }

#[no_mangle]
fn return_string()->&'static str{ return "This works!"; }
