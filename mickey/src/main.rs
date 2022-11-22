#![allow(unused)]

use std::env;
use std::fs;
use clap::Parser;
use  std::process::Command;

#[derive(Parser)]
struct Cli {
    cmd: String
}

fn apply() {
    Command::new("sh")
            .arg("-c")
            .arg("terraform -chdir=$MICKEY_TF_PATH apply")
            .spawn()
            .expect("failed to execute ~ terraform apply ~");
}

fn main() {

    let args     = Cli::parse();
    let command  = &args.cmd;

    if command.eq("list-resources") {
        let out = Command::new("sh")
            .arg("-c")
            .arg("terraform state list -state=$MICKEY_TF_PATH/terraform.tfstate")
            .output()
            .expect("failed to execute ~ terraform state list ~");
        println!("\n{}", String::from_utf8_lossy(&out.stdout));
    }
    else if command.eq("create-vpc") {
        let tf_path = match env::var("MICKEY_TF_PATH") {
            Ok(val) => val,
            Err(_e) => "none".to_string(),
        };

        let path = format!("{}/mickey.json", tf_path);
        let data = fs::read_to_string(path)
        .expect("Unable to read file");

        let json: serde_json::Value = serde_json::from_str(&data)
        .expect("JSON does not have correct format.");

        dbg!(&json["instances"]);

        dbg!(json);
        // apply();
    }
    else if command.eq("create-subnet") {

    }
    else if command.eq("create-instance") {

    }
    else if command.eq("destroy-instance") {

    }
    else if command.eq("create-security-group") {

    }
    else if command.eq("destroy-security-group") {

    }
    else { println!("command ~ {} ~ not found", command) }
}